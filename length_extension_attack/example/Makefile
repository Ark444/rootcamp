##
## Makefile for hash ext attack in /home/roland_q/Secu/rootcamp/length_extension_attack/example
## 
## Made by roland_q
## Login   <roland_q@epitech.net>
## 
## Started on  Tue Apr 22 23:51:44 2014 roland_q
## Last update Wed Apr 23 22:08:10 2014 roland_q
##

MAC			=	mac
CHECK			=	check

CC			=	gcc
RM			=	rm -f
LN			=	ln -sf

CFLAGS			=	-W -Wall -Wextra -O3 -std=gnu99 -Werror
LDFLAGS			=	-lbsd

MAC_SRC			=	$(MAC).c
MAC_OBJ			=	$(MAC_SRC:.c=.o)

CHECK_SRC		=	$(CHECK).c
CHECK_OBJ		=	$(CHECK_SRC:.c=.o)

all:		$(MAC) $(CHECK)

$(MAC):		$(MAC_OBJ)
		$(CC) $(MAC_OBJ) $(LDFLAGS) -o $(MAC)

$(CHECK):	$(CHECK_OBJ)
		$(CC) $(CHECK_OBJ) $(LDFLAGS) -o $(CHECK)

clean:
	$(RM) $(MAC_OBJ)
	$(RM) $(CHECK_OBJ)

fclean:	clean
	$(RM) $(MAC)
	$(RM) $(CHECK)

re:	fclean all
