class GFG 
{ 
    static double medianOfArrays(int n, int m, int a[], int b[]) 
    {
        ArrayList<Integer> list = new ArrayList<>();
        int i = 0, j = 0;
        while(i < n && j < m) {
            if (a[i] <= b[j]) {
                list.add(a[i]);
                i++;
            } else {
                list.add(b[j]);
                j++;
            }
            if (list.size() > (n + m) / 2) break;
        }
        while (i < n && list.size() <= (n + m) / 2) {
            list.add(a[i]);
            i++;
        }
        while (j < m && list.size() <= (n + m) / 2) {
            list.add(b[j]);
            j++;
        }
        
        int totalSize = n + m;
        if (totalSize % 2 == 0) {
            return (list.get(totalSize / 2 - 1) + list.get(totalSize / 2)) / 2.0;
        } else {
            return list.get(totalSize / 2);
        }
    }
}
