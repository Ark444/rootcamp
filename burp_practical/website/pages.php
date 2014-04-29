<?php
header('Content-Type: application/json');
if (!empty($_GET['page']) && is_string($_GET['page'])) {
	$requested_page = strtolower($_GET['page']);
	if ($requested_page == 'members') {
		$body = <<<EOF
	<div class="panel panel-default">
	  <div class="panel-heading">Members</div>

	  <!-- Table -->
	  <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Username</th>
            <th>Role</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>1</td>
            <td>BestPig</td>
            <td>user</td>
          </tr>
          <tr>
          	<td>2</td>
            <td>Anonymous</td>
            <td>user</td>
          </tr>
        </tbody>
      </table>
	</div>
EOF;
	}
	else if ($requested_page == 'contact') {
		$body = <<<EOF
		<div class="well">
			Sorry but I don't want to be contacted<br /><br />
			<img src="img/pig.png" alt="BestPig">
		</div>
EOF;
	}
}
if (!isset($body)) {
	$body = <<<EOF
	<div class="jumbotron">
	  <h1>Welcome!</h1>
	  <p>This new kind of website if fully ajaxed :D</p>
	</div>
EOF;
}
echo json_encode(array('container'=>base64_encode(implode("\n", array_map("strrev", explode("\n", $body))))));