
#include <string.h>
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <bsd/md5.h>
#include <arpa/inet.h>

void
hexdigest(unsigned char mac[MD5_DIGEST_LENGTH]) {
  for (int i = 0; i < 16; i++) {
    printf("%02x", mac[i]);
  }
  printf("\n");
}

int
main(int argc, char *argv[]) {

  unsigned char mac[MD5_DIGEST_LENGTH];
  MD5_CTX ctx;

  if (argc != 2) {
    printf("Usage: %s <append_message>\n", *argv);
    return 1;
  }

  MD5Init(&ctx);

  /*
     md5 blocks are 64 bytes long
     So let's write on a full block
  */
  MD5Update(&ctx, (const u_int8_t *) "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA", 64);

  /*
    Then we initializes the context with the good hash values
    so we can have the good hash as if we were using the SECRET
    Using htonl to convert into good endianness form :)
  */

  ctx.state[0] = htonl(0x61f5d0d9);
  ctx.state[1] = htonl(0xbacfbb89);
  ctx.state[2] = htonl(0x394b3cc0);
  ctx.state[3] = htonl(0x93a65153);

  /*
    We can now update with our appended text
  */

  MD5Update(&ctx, (const u_int8_t *) argv[1], strlen(argv[1]));

  MD5Final(mac, &ctx);
  hexdigest(mac);

  return 0;
}
