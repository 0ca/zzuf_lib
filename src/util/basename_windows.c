//Source: https://www.thecodingforums.com/threads/plattform-independent-basename-function.666522/
#if defined _WIN32 || defined __WIN32__ || defined __EMX__ || defined __DJGPP__
/* Win32, OS/2, DOS */
# define HAS_DEVICE(P) \
((((P)[0] >= 'A' && (P)[0] <= 'Z') || ((P)[0] >= 'a' && (P)[0] <= 'z')) \
&& (P)[1] == ':')
# define FILESYSTEM_PREFIX_LEN(P) (HAS_DEVICE (P) ? 2 : 0)
# define ISSLASH(C) ((C) == '/' || (C) == '\\')
#endif

#ifndef FILESYSTEM_PREFIX_LEN
# define FILESYSTEM_PREFIX_LEN(Filename) 0
#endif

#ifndef ISSLASH
# define ISSLASH(C) ((C) == '/')
#endif

char *
basename(char const *name)
{
	char const *base = name += FILESYSTEM_PREFIX_LEN(name);
	int all_slashes = 1;
	char const *p;

	for (p = name; *p; p++)
	{
		if (ISSLASH(*p))
			base = p + 1;
		else
			all_slashes = 0;
	}

	/* If NAME is all slashes, arrange to return `/'. */
	if (*base == '\0' && ISSLASH(*name) && all_slashes)
		--base;

	/* Make sure the last byte is not a slash. */
	//assert(all_slashes || !ISSLASH(*(p - 1)));

	return (char *)base;
}

