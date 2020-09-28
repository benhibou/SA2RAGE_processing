/****************************************
** unravel.c
** To read the result of the processing
** of a SA2RAGE experiment and compare
** it with the values obtained through
** Bloch equation simulation so as to
** assign to each pixel a T1 value.
******************************************/


#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

double * unrav ( double *, double *, double *, int *, int * );

int 	main ( int argc, char ** argv )
{
	FILE	* fp, * gp, * hp;
	void	* ptr;
	int	i, j, k, ni, readpt, nlin;
	char 	** filnam;
	double	* l, * m, * mpint, * T1;

        /* The file containing the SA2RAGE experimental intensities */
	if ( ( ( fp = fopen ( * ++argv, "r" ) ) == 0 ) ) {
	   perror ( "Error reading fp" );
	   exit ( 1 );
 	}
	readpt = atoi ( *++argv );

        /* The file containing the SA2RAGE intensities as a function of B1 */
	if ( ( ( gp = fopen ( * ++argv, "r" ) ) == 0 ) ) {
	   perror ( "Error reading gp" );
	   exit ( 1 );
 	}

	nlin = atoi ( *++argv );

	mpint = ( double * ) malloc ( nlin * sizeof ( double ) );
	T1 = ( double * ) malloc ( nlin * sizeof ( double ) );
        i = 0;
        j = 0;
        while ( 1 ) {
            if ( ( i = fscanf ( gp, "%lf %lf\n",  mpint + j, T1 + j ) ) != 2 ) {
               break; 
            }
            j++;
        }
        fclose ( gp );
	
	/*hp = ( FILE * ) malloc ( sizeof ( FILE ) );*/
	if ( ( ( hp = fopen ( * ++argv, "w" ) ) == 0 ) ) {
	   perror ( "Error opening File T1map for write" );
	   exit ( 1 );
 	}

	ptr = ( double * ) malloc ( readpt * sizeof ( double ) );
	m = ( double * ) malloc ( readpt * sizeof ( double ) );
	i = 1;
	j = 0;
	k = 0;
	m = 0;
	while ( 1 ) {
	    i = fread ( ptr, sizeof ( double ), readpt, fp );
	    if ( i < 1 ) {
	       break;
	    }
	    l = ptr;
            /*for ( i = 0 ; i < readpt ; i++ ) {
                printf ( "%d\t%f\n", i, l[i] );
            }*/
            m = unrav ( l, mpint, T1, & readpt, & nlin ); 
	    fwrite ( m, sizeof ( double ), readpt, hp );
	}
	fclose ( fp );
	free ( ptr );
        free ( m );
	return 1;
}

double	* unrav ( double * l, double * mpint, double * T, int * readpt, int * nlin )
{
        int	i, j;
        double  * m;
        
        printf ( "%d\t%d\n",*readpt, *nlin);
	m = ( double * ) malloc ( (* readpt ) * sizeof ( double ) );
        for ( i = 0; i < * readpt; i++ ) {
            m[i] = 5;
            for ( j = 0; j < * nlin; j++ ) {
                if ( l[i] < mpint[j] ) {
                   ;
                } 
                else {
                   m[i] = T[j];
                   break;
                 printf ( "%lf\t%lf\n",m[i], l[i]);
                } 
	    }
        }
        return m;
}
