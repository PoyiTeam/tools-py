功能: 自動畫出confunsion matrix，並儲存

input: confusion_matrix, fig_title, saving_path

confusion_matrix:pandas dataframe

範例格式

Predicted   0   1   2   3   4   5   6   7   8   9
Actual                                           
0          75   0   0   0   0   0   0   0   0   0
1           0  75   0   0   0   0   0   0   0   0
2           0   0  75   0   0   0   0   0   0   0
3           0   2   0  69   3   0   1   0   0   0
4           0   0   0   0  75   0   0   0   0   0
5           0   0   0   0   0  75   0   0   0   0
6           0   0   0   0   0   0  75   0   0   0
7           0   0   0   0   0   0   0  75   0   0
8           0   0   0   0   0   0   0   0  75   0
9           0   0   0   0   0   0   0   0   0  75


fig_title: string

saving_path: string