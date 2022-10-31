#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void swap(int *x, int *y) {
	int t = *x;

	*x = *y;
	*y = t;
}

int partition(int *z, int l, int r) {
    int p = z[l];
    int i = l + 1;
    int j = r;

    while(j <= i){
        while ((i < r) && (z[i] <= p)){i += 1;} 
        while ((j > l) && (z[i] >= p)){j -= 1;} 
        if (i < j){
            swap(&z[i],&z[j]);
        }
    }
    swap(&z[i],&z[l]);
    return j;
}

void qs(int *z, int l, int r) {
    
}

int cmp(const void *a, const void *b) {
	int x = *(int *) a;
	int y = *(int *) b;

	return x - y;
}

int main(void) {
	clock_t t1, t2, t3, t4;
	double diff1, diff2;
	int n, *zahlen1, *zahlen2;

	printf("%10s: %7s\t%7s\n", "n", "stdlib", "own proc");
	for (n = (1 << 15); n <= (1 << 27); n *= 2) {
		int i;

		zahlen1 = (int *) malloc(n * sizeof(int));
		zahlen2 = (int *) malloc(n * sizeof(int));
		for (i = 0; i < n; i++) {
			zahlen1[i] = rand() * 10000 + rand();
			zahlen2[i] = zahlen1[i];
		}

		t1 = clock();
		qsort(zahlen1, n, sizeof(int), cmp);
		t2 = clock();
		diff1 = t2 - t1;
		diff1 /= CLOCKS_PER_SEC;

		t3 = clock();
		qs(zahlen2, 0, n-1);
		t4 = clock();
		diff2 = t4 - t3;
		diff2 /= CLOCKS_PER_SEC;

		printf("%10d: %7.1f\t%7.1f\n", n, diff1, diff2);

		free(zahlen1);
		free(zahlen2);
	}

	return 0;
}
