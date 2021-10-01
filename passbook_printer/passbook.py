class bank:
    z=int(input('Enter the no of transaction:'))
    cr=[]
    db=[]
    st=[]
    bl=[]
    tn=[]
    def statement(self):
        import time
        global z
        self.balance=10000
        for i in range(1,bank.z+1):
          print('-----------------------')
          print('Welcome to Johnson bank')
          print('-----------------------')
          print('Transaction no:',i)
          print('Enter the type of transtion:')
          Choice=int(input('(1-credit,2-debit) Enter your choice:'))
          if Choice==1:
              creditamount=float(input('Enter the amount to credit:'))
              bank.cr.append(creditamount)
              bank.db.append(0)
              bank.st.append('cr')
              self.balance+=creditamount
              bank.bl.append(self.balance)
              bank.tn.append(time.ctime())
          elif Choice==2:
              debitamount=float(input('Enter the amount to debit:'))
              if (debitamount>self.balance):
                  print('Insufficient balance')
              else:
                  bank.cr.append(0)
                  bank.db.append(debitamount)
                  bank.st.append('dr')
                  self.balance-=debitamount
                  bank.bl.append(self.balance)
                  bank.tn.append(time.ctime())
          else:
              print('wrong input. Restart the proces ')
              
b=bank()

b.statement()

class passbook(bank):
    def book(statement):
        print(' ___________________________________________________________________________________________')
        print('|                                                                                           |')
        print('|                             Johnson Bank-Passbook Details                                 |')
        print('|___________________________________________________________________________________________|')
        print('Opening Balance=10000Rs')
        print('.............................................................................................')
        print('Type         Credit           Debit            Balance(Rs)                Time           ')
        print('.............................................................................................')
        for i in range(0,bank.z):
            status=bank.st[i]
            credit=bank.cr[i]
            debit=bank.db[i]
            balance=bank.bl[i]
            time=bank.tn[i]
            print(status,' '*9,credit,' '*11,debit,' '*12,balance,' '*12,time)
        print('.............................................................................................')
        print('                                         Thank You                                           ')

p=passbook()
p.book()



        


              

              
