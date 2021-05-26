#!/usr/bin/env python
# coding: utf-8

# In[4]:


import payslip 

tax = payslip.read_tax('tax.txt')
employee = payslip.read_employee('Emp1.txt')
payslip1 = payslip.reciept('Hours.txt',tax,employee)
print(payslip1)


# In[ ]:




