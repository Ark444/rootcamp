
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <bsd/md5.h>
#include <arpa/inet.h>

#define SECRET "HashExtAttack"

void
shexdigest(unsigned char *buf, unsigned char mac[MD5_DIGEST_LENGTH]) {
  for (int i = 0; i < 16; ++i) {
    sprintf((char *)(buf + (i * 2)), "%02x", mac[i]);
  }
}

int
lstrstr(char *s1, int l1, char *s2, int l2) {
  int i, j;

  j = 0;
  for (i = 0 ; i < l1 ; ++i) {
    for (j = 0 ; j < l2 && s1[i + j] == s2[j]; ++j);
    if (j == l2)
      return 0;
  }
  return -1;
}

int
main(int argc, char *argv[]) {

  char buffer[1024];
  unsigned char mac[MD5_DIGEST_LENGTH];
  unsigned char buf[MD5_DIGEST_STRING_LENGTH];
  MD5_CTX ctx;
  int ret;

  if (argc != 2) {
    printf("Usage: %s <mac>\n", *argv);
    return 1;
  }

  ret = read(0, buffer, 1024);
  if (ret == -1)
    return 1;

  printf("User message = [%s]\n", buffer);
  printf("User mac = [%s]\n", argv[1]);

  MD5Init(&ctx);
  MD5Update(&ctx, (const u_int8_t *) SECRET, strlen(SECRET));
  MD5Update(&ctx, (const u_int8_t *) buffer, ret);
  MD5Final(mac, &ctx);

  shexdigest(buf, mac);
  printf("[Hint] Expected mac = [%s]\n", buf);

  if (!strcmp((char *)buf, argv[1]) && !lstrstr(buffer, ret, "flag", 4))
    printf("Good!\n");
  else
    printf("Nope\n");

  return 0;
}
