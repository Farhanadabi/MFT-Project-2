from tkinter import *
import sqlite3 as sq
from tkinter import messagebox
import os
global cnt
cnt = 0
#create directory
path = 'c:/mft'
try:
    os.mkdir(path)
    print('Folder Created')
except FileExistsError:
    print ('Folder Already Exist In  ' +  path)



#DATABASE
try:
    cn = sq.connect('C:/mft/data.db')
    print('Successfully Connected ✔ '+'\n')
except:
    print('Error')
try:

    cn.execute(''' CREATE TABLE DATA 
               (ID INTEGER PRIMARY KEY,
                USER TEXT NOT NULL,
                PASS TEXT NOT NULL,
                );''')
    print('Table Created Successfully ✔ ')
except:
    print('Table ✔ '+'\n')


def root():
    
    global ws
    ws = Tk()
    ws.title('MFT Project')
    ws.geometry('960x540')
    ws.config(bg='#12181E')
    widgets()
def widgets():
    global lbl
    global login_btn
    global reg_btn
    global del_btn
    global exit_btn
    lbl=Label(ws,text='Login Or Register',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    lbl.pack()
    Label(text="",bg='#12181E').pack()
    Label(text="",bg='#12181E').pack()
    Label(text="",bg='#12181E').pack()
    
    #buttons
    login_btn=Button(ws,text='Login',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_login,bd=0,activebackground='#4B6EAD')
    login_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    reg_btn=Button(ws,text='Register',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_register,bd=0,activebackground='#4B6EAD')
    reg_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    del_btn=Button(ws,text='Delete Account',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_delete_account,bd=0,activebackground='#4B6EAD')
    del_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    exit_btn=Button(ws,text='Exit',height="2",font=('',13,'bold'), width="30",fg='white',bg='#6495ED',command=ws.destroy,bd=0,activebackground='#4B6EAD')
    exit_btn.pack()
    ws.mainloop()
def destroy_to_login():
    try:
        for i in ws.winfo_children():
            i.forget()
        login_page()
    except:
        pass
def destroy_to_main():
    try:
        for i in ws.winfo_children():
            i.forget()
        widgets()
    except:
        pass
def destroy_to_register():
    try:
        for i in ws.winfo_children():
            i.forget()
        register_page()
    except:
        pass
def destroy_to_delete_account():
    try:
        for i in ws.winfo_children():
            i.forget()
        delete_account_page()
    except:
        pass

def login_page():
    #globalize
    global lgn_ent
    global lgn_pw_ent
    global lgn_msg
    global lgn_btn
    #labels
    lgn_top=Label(ws,text='Login Page',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    lgn_top.pack()
    
    lgn_user_lbl=Label(ws,text='Username:',font=("default",15),fg='green',bg='#12181E')
    lgn_user_lbl.pack()
    #Entry
    
    lgn_ent=Entry(ws,width=21,font=("default",19))
    lgn_ent.pack()
    
    lgn_password_lbl=Label(ws,text='Password:',font=("default",15),fg='green',bg='#12181E')
    lgn_password_lbl.pack()
    
    
    lgn_pw_ent=Entry(ws,width=21,font=("default",19),show='*')
    lgn_pw_ent.pack()
    
    Label(text="",bg='#12181E').pack()
    #buttons
    lgn_btn=Button(ws,text='Login',height="2",font=('',11,'bold'), width="30",fg='white',bg='#51E79D',command=verify_login,bd=0,activebackground='#41A071')
    lgn_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    bck_btn=Button(ws,text='back',height="2",font=('default',9,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_main,bd=0,activebackground='#4B6EAD')
    bck_btn.pack()
    
    lgn_msg=Label(ws,text='',fg='red',bg='#12181E')
    lgn_msg.pack()
def register_page():
    #globalize
    global reg_ent
    global reg_pw_ent
    global reg_msg
    #labels
    reg_st=Label(ws,text='Register Page',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    reg_st.pack()
    
    reg_username_lbl=Label(ws,text='Username:',font=("default",15),fg='green',bg='#12181E')
    reg_username_lbl.pack()
    #Entry
    
    reg_ent=Entry(ws,width=21,font=("default",19))
    reg_ent.pack()
    
    reg_password_lbl=Label(ws,text='Password:',font=("default",15),fg='green',bg='#12181E')
    reg_password_lbl.pack()
    
    
    reg_pw_ent=Entry(ws,width=21,font=("default",19),show='*')
    reg_pw_ent.pack()
    
    Label(text="",bg='#12181E').pack()
    #buttons
    reg_btn=Button(ws,text='Register',height="2",font=('',11,'bold'), width="30",fg='white',bg='#51E79D',command=register_user,bd=0,activebackground='#41A071')
    reg_btn.pack()
    
    Label(text="",bg='#12181E').pack()
    
    bck_btn=Button(ws,text='back',height="2",font=('default',9,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_main,bd=0,activebackground='#4B6EAD')
    bck_btn.pack()
    
    reg_msg=Label(ws,text='',fg='red',bg='#12181E')
    reg_msg.pack()
def delete_account_page():
    #globalize
    global del_ent
    global del_pw_ent
    global del_msg
    #labels
    del_st=Label(ws,text='Delete Account Page',font=('Segoe Print',30,'bold'),width=100,height=2,fg='cyan',bg='#12181E')
    del_st.pack()
    
    del_username_lbl=Label(ws,text='Username:',font=("default",15),fg='green',bg='#12181E')
    del_username_lbl.pack()
    #Entry
    
    del_ent=Entry(ws,width=21,font=("default",19))
    del_ent.pack()
    
    del_password_lbl=Label(ws,text='Password:',font=("default",15),fg='green',bg='#12181E')
    del_password_lbl.pack()
    
    
    del_pw_ent=Entry(ws,width=21,font=("default",19),show='*')
    del_pw_ent.pack()
    
    Label(text="",bg='#12181E').pack()
    #buttons
    del_btn=Button(ws,text='Delete Account',height="2",font=('',11,'bold'), width="30",fg='white',bg='#51E79D',command=delete_user,bd=0,activebackground='#41A071')
    del_btn.pack()
    
    
    Label(text="",bg='#12181E').pack()
    
    bck_btn=Button(ws,text='back',height="2",font=('default',9,'bold'), width="30",fg='white',bg='#6495ED',command=destroy_to_main,bd=0,activebackground='#4B6EAD')
    bck_btn.pack()
    
    del_msg=Label(ws,text='',fg='red',bg='#12181E')
    del_msg.pack()

def verify_login():
    global cnt
    u = lgn_ent.get()
    p = lgn_pw_ent.get()

    try:

        check = cn.execute("SELECT USER,PASS FROM DATA WHERE USER=? AND PASS=?",(u,p))
        check = check.fetchone()
        
        if check != None:
            lgn_msg.configure(text='Welcome',fg="green")
        else:
            cnt+=1
            lgn_msg.configure(text='Wrong Username Or Password!',fg="red")
        if cnt>=3:
            lgn_msg.configure(text='3 times cooldown')
            lgn_btn.configure(state='disabled')
            lgn_btn.after(3000,lambda:lgn_btn.configure(state='normal'))
            lgn_msg.after(3100,lambda:lgn_msg.configure(text=''))
            cnt=0


            
        

    except:
        print('bad working..')
        

def register_user():
    u = reg_ent.get()
    p = reg_pw_ent.get()
    try:

        check = cn.execute("SELECT USER,PASS FROM DATA WHERE USER=? ",(u,))
        check = check.fetchone()
    
        if check==None:
            cn.execute('''INSERT INTO DATA (USER,PASS)
            VALUES (?,?)''',(u,p))
            cn.commit()
            reg_msg.configure(text='Successfully Submited ✔ ',fg="green")
        else:
            reg_msg.configure(text='Username Already Exist!',fg="red")
    except:
        print('Problem...')
def delete_user():
    global check
    u = del_ent.get()
    p = del_pw_ent.get()


    try:

        check = cn.execute("SELECT USER,PASS FROM DATA WHERE USER=? AND PASS=?",(u,p))
        check = check.fetchone()


        if check!=None:
                print('Verified ✔')
                confirm()
        else:
            del_msg.configure(text='Wrong Username Or Password !',fg='red')
            
    except:
        pass
def confirm():
    try:

        msg_box = messagebox.askquestion('Confirmation','Are You Sure?')
        if msg_box == 'yes' :

            de = cn.execute("DELETE FROM DATA  WHERE USER=? AND PASS=?",(check[0],check[1]))
            cn.commit()
            del_msg.configure(text='Successfully Deleted ✔',fg="green")
        elif msg_box == 'no' :
            pass
    except:
        pass
root()
#1.42
