print("Hey there ")
print("1.Enployee")
print("2.Adminstrator")
choice=int(input("Enter Your choice: "))



if choice==1:                                           ## Employee section
    row=[0,0,0,0,0,1,0,0,0]
    dep=['sales', 'accounting', 'hr', 'technical', 'support', 'management',
        'IT', 'product_mng', 'marketing', 'RandD']

    from tkinter import *
    root=Tk()
    root.title("Employee")
    root.geometry("800x800")

    Label(root, text="Please fill the work experience form ",font="ar 15 bold").grid(row=0,column=3)

    satis_level=Label(root,text="Satisfaction level").grid(row=1,column=2)
    last_eval=Label(root,text="Last Evaluation").grid(row=2,column=2)
    noofproj=Label(root,text="number of project").grid(row=3,column=2)
    avgmonthlyhr=Label(root,text="average monthly hours").grid(row=4,column=2)
    time_spent=Label(root,text="Time spent(years)").grid(row=5,column=2)
    work_accident=Label(root,text="Work Accident").grid(row=6,column=2)
    promotion=Label(root,text="promotions in last 5 years").grid(row=7,column=2)
    department=Label(root,text="Department").grid(row=8,column=2)
    # salary=Label(root,text="salary")


    satis_levelval=IntVar
    last_evalval=IntVar
    noofprojval=IntVar
    avgmonthlyhrval=IntVar
    time_spentval=IntVar
    work_accidentval=IntVar
    promotionval=IntVar
    var=StringVar



    sasentry=Entry(root, textvariable=satis_levelval).grid(row=1,column=3)
    evaluentry=Entry(root,textvariable=last_evalval).grid(row=2,column=3)
    nopentry=Entry(root,textvariable=noofprojval).grid(row=3,column=3)
    avegtimeentry=Entry(root,textvariable=avgmonthlyhrval).grid(row=4,column=3)
    timeentry=Entry(root, textvariable=time_spentval).grid(row=5,column=3)
    worksccentry=Entry(root,textvariable=work_accidentval).grid(row=6,column=3)
    promoentry=Entry(root,textvariable=promotionval).grid(row=7,column=3)

    radio=Radiobutton(root,text='sales',padx=14,variable=var,value="sales").grid(row=8,column=3)
    radio=Radiobutton(root,text='sales',padx=14,variable=var,value="sales").grid(row=8,column=3)
    radio=Radiobutton(root,text='sales',padx=14,variable=var,value="sales").grid(row=8,column=3)
    radio=Radiobutton(root,text='sales',padx=14,variable=var,value="sales").grid(row=8,column=3)
    radio=Radiobutton(root,text='sales',padx=14,variable=var,value="sales").grid(row=8,column=3)
    radio=Radiobutton(root,text='sales',padx=14,variable=var,value="sales").grid(row=8,column=3)
    radio=Radiobutton(root,text='sales',padx=14,variable=var,value="sales").grid(row=8,column=3)


    root.mainloop()

    from csv import writer

    my_file="dataset.csv"
    with open(my_file,"a") as f_obj:
        writer_object=writer(f_obj)
        writer_object.writerow(row)
        f_obj.close()

elif choice==2:
    import numpy as np
    import pandas as pd

    df = pd.read_csv('dataset.csv')
    df = df.rename(columns={'sales' : 'department'})
    df['department']=np.where(df['department'] =='support', 'technical', df['department'])
    depart = pd.get_dummies(df['department'], prefix='department', drop_first=True )
    sales = pd.get_dummies(df['salary'], prefix='salary', drop_first=True )
    df = df.join(depart)
    df = df.join(sales)
    cols = ['department', 'salary']
    df.drop(cols, axis=1, inplace=True)
    X = df.drop('left', axis=1)       # X is complete dataframe except "left" column 
    y = df['left']                    # y holds the "left" column

    new_cols = ['satisfaction_level', 'last_evaluation', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 'department_RandD',
        'department_hr', 'department_management', 'salary_low', 'salary_medium']

    X = df[new_cols]
    y = df['left']

    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.3, random_state=92)

    from sklearn.ensemble import RandomForestClassifier

    model_rf = RandomForestClassifier()

    model_rf.fit(X_train, y_train)

    feature_labels = np.array(['satisfaction_level', 'last_evaluation', 'time_spend_company', 'Work_accident', 'promotion_last_5years', 
        'department_RandD', 'department_hr', 'department_management', 'salary_high', 'salary_low'])
    importance = model_rf.feature_importances_
    for i in range(10):
        importance[i]=(round((importance[i] *100.0),2))
    # feature_indexes_by_importance = importance.argsort()
    # for index in feature_indexes_by_importance:
    #     print('{}    -> {:.2f}%'.format(feature_labels[index], (importance[index] *100.0)))
    
    from tkinter import *
    root=Tk()
    root.title("Adminstrator")
    root.geometry("600x400")

    warti=Label(root,text="Following are the Reasons for Employee turnover",font="ar 15 bold").grid(row=0,column=3)

    sat=Label(root,text=("satisfaction_level -->",importance[0])).grid(row=2,column=3)
    lev=Label(root,text=("last_evaluation -->",importance[1] )).grid(row=3,column=3)
    tcs=Label(root,text=("time_spend_company -->",importance[2])).grid(row=4,column=3)
    wa=Label(root,text=("Work_accident -->",importance[3])).grid(row=5,column=3)
    pl5=Label(root,text=("promotion_last_5years -->",importance[4])).grid(row=6,column=3)
    drnd=Label(root,text=("department_RandD -->",importance[5])).grid(row=7,column=3)
    dhr=Label(root,text=("department_hr -->",importance[6])).grid(row=8,column=3)
    dm=Label(root,text=("department_management -->",importance[7])).grid(row=9,column=3)
    salh=Label(root,text=("salary_high-->",importance[8])).grid(row=10,column=3)
    sall=Label(root,text=("salary_low -->",importance[9])).grid(row=11,column=3)
    
    
    
    root.mainloop()


