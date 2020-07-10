import pandas as pd

df_old = pd.read_excel('공공KOLASIII0617.xlsx')
df_new = pd.read_excel('공공KOLASIII0622.xlsx')

df_old['ver'] = 'old'
df_new['ver'] = 'new'

id_dropped = set(df_old['LIB_CODE']) - set(df_new['LIB_CODE'])
id_added = set(df_new['LIB_CODE']) - set(df_old['LIB_CODE'])

df_dropped = df_old[df_old['LIB_CODE'].isin(id_dropped)].iloc[:,:-1]
df_added = df_new[df_new['LIB_CODE'].isin(id_added)].iloc[:,:-1]

# 두 데이터프레임을 하나로 합칩니다.
df_concatted = pd.concat([df_old, df_new], ignore_index=True)
# 모든 컬럼의 내용이 중복되는 데이터는 삭제합니다.
changes = df_concatted.drop_duplicates(df_concatted.columns[:-1], keep='last')

# 남은 데이터 중 동일한 아이디 값이 두개 이상 존재한다면
# 정보가 변경된 데이터입니다.
duplicated_list = changes[changes['LIB_CODE'].duplicated()]['LIB_CODE'].to_list()
df_changed = changes[changes['LIB_CODE'].isin(duplicated_list)]

df_changed_old = df_changed[df_changed['ver'] == 'old'].iloc[:,:-1]
df_changed_old.sort_values(by='LIB_CODE', inplace=True)

df_changed_new = df_changed[df_changed['ver'] == 'new'].iloc[:,:-1]
df_changed_new.sort_values(by='LIB_CODE', inplace=True)

df_info_changed = df_changed_old.copy()
for i in range(len(df_changed_new.index)):
    for j in range(len(df_changed_new.columns)):
        if(df_changed_new.iloc[i, j] != df_changed_old.iloc[i, j]):
            df_info_changed.iloc[i, j] = str(df_changed_old.iloc[i, j]) + " ==> " + str(df_changed_new.iloc[i,j])

with pd.ExcelWriter('compared_result.xlsx') as writer:
    df_info_changed.to_excel(writer, sheet_name='info chaged', index_label=False)
    df_added.to_excel(writer, sheet_name='added', index=False)
    df_dropped.to_excel(writer, sheet_name='dropped')

