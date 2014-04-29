# Burp Ajaxed Practical Extension - By BestPig
# ---
# Based on Burp Extension - JSON decoder
# Copyright : Michal Melewski <michal.melewski@gmail.com>

import json
import base64

from burp import IBurpExtender
from burp import IMessageEditorTabFactory
from burp import IMessageEditorTab


class BurpExtender(IBurpExtender, IMessageEditorTabFactory):
    def registerExtenderCallbacks(self, callbacks):
        self._callbacks = callbacks
        self._helpers = callbacks.getHelpers()

        callbacks.setExtensionName('Ajaxed Decoder')
        callbacks.registerMessageEditorTabFactory(self)

    def createNewInstance(self, controller, editable):
        return AjaxedDecoderTab(self, controller, editable)


class AjaxedDecoderTab(IMessageEditorTab):
    def __init__(self, extender, controller, editable):
        self._extender = extender
        self._helpers = extender._helpers
        self._editable = editable

        self._txtInput = extender._callbacks.createTextEditor()
        self._txtInput.setEditable(editable)

    def getTabCaption(self):
        return "Ajaxed Decoder"

    def getUiComponent(self):
        return self._txtInput.getComponent()

    def isEnabled(self, content, isRequest):
        if isRequest:
            r = self._helpers.analyzeRequest(content)
        else:
            r = self._helpers.analyzeResponse(content)

        for header in r.getHeaders():
            if header.lower().startswith("content-type:"):
                content_type = header.split(":")[1].lower()
                if content_type.find("application/json") > 0:
                    return True
                else:
                    return False

        return False

    def setMessage(self, content, isRequest):
        if content is None:
            self._txtInput.setText(None)
            self._txtInput.setEditable(False)
        else:
            if isRequest:
                r = self._helpers.analyzeRequest(content)
            else:
                r = self._helpers.analyzeResponse(content)

            msg = content[r.getBodyOffset():].tostring()
            try:
                decoded = base64.b64decode(json.loads(msg)["container"])
                pretty_msg = "\n".join(map(lambda x: x[::-1],
                                       decoded.split('\n')))
            except:
                pretty_msg = msg

            self._txtInput.setText(pretty_msg)
            self._txtInput.setEditable(self._editable)

        self._currentMessage = content

    def getMessage(self):
        if self._txtInput.isTextModified():
            msg = self._helpers.bytesToString(self._txtInput.getText())
            try:
                encoded = base64.b64encode("\n".join(map(lambda x: x[::-1],
                                                         msg.split('\n'))))
                data = json.dumps({"container": encoded})
            except Exception:
                data = msg

            # Reconstruct request/response
            r = self._helpers.analyzeRequest(self._currentMessage)
            data_bytes = self._helpers.stringToBytes(data)
            return self._helpers.buildHttpMessage(r.getHeaders(), data_bytes)
        else:
            return self._currentMessage

    def isModified(self):
        return self._txtInput.isTextModified()

    def getSelectedData(self):
        return self._txtInput.getSelectedText()
