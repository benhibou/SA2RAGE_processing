/****************************************
** extr_mp2r.c
** Extract data from a complex 2dseq
** file and distribute it into two real
** and imaginary type of files.
******************************************/


#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int 	main ( int argc, char ** argv )
{
	FILE	* fp, ** hp;
	void	* ptr;
	int	i, j, k, m, ni, readpt, phase1pt, phase2pt;
	char 	** filnam;
	short	* l;

	if ( ( ( fp = fopen ( * ++argv, "r" ) ) == 0 ) ) {
	   perror ( "Error reading fp" );
	   exit ( 1 );
 	}
	readpt = atoi ( *++argv );
	ni = 4;
	
	hp = ( FILE ** ) malloc ( ni * sizeof ( FILE * ) );
	filnam = ( char ** ) malloc ( ni * sizeof ( char * ) );
	for ( i = 0 ; i < ni ; i++ ) {
	    hp[i] = ( FILE * ) malloc ( sizeof ( FILE ) );
	    filnam[i] = ( char * ) malloc ( 12 * sizeof ( char ) );
            if ( i == 0 ) {
	       if ( sprintf ( filnam[i], "fid_1r" ) == EOF ) {
	          perror ( "Copying filename" );
	          exit ( 1 );
	       }
            }
            else if ( i == 1 ){
	       if ( sprintf ( filnam[i], "fid_2r" ) == EOF ) {
	          perror ( "Copying filename" );
	          exit ( 1 );
	       }
            }
            if ( i == 2 ) {
	       if ( sprintf ( filnam[i], "fid_1i" ) == EOF ) {
	          perror ( "Copying filename" );
	          exit ( 1 );
	       }
            }
            else if ( i == 3 ){
	       if ( sprintf ( filnam[i], "fid_2i" ) == EOF ) {
	          perror ( "Copying filename" );
	          exit ( 1 );
	       }
            }
	    if ( ( ( hp[i] = fopen ( filnam[i], "w" ) ) == 0 ) ) {
	       perror ( "Error opening File 2dseq_i for write" );
	       exit ( 1 );
 	    }
	}

	ptr = ( short * ) malloc ( readpt * sizeof ( short ) );
	i = 1;
	j = 0;
	k = 0;
	m = 0;
	while ( 1 ) {
	    i = fread ( ptr, sizeof ( short ), readpt, fp );
	    if ( i < 1 ) {
	       break;
	    }
	    l = ptr;
	    fwrite ( l, sizeof ( short ), readpt, hp[k] );
	    j++;
	    k++;
	    if ( k == ni ) {
	       k = 0;
            }
	}
	fclose ( fp );
	free ( ptr );
	free ( hp );
	free ( filnam );
	return 1;
}
