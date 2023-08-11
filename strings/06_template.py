letter=''' Dear <|NAME|>
 We are pleased to offer you the full-time position of Product Manager  contingent upon a background check. [manager/supervisor name] at [workplace location] will be your primary contact and manager on site. It is in our opinion that your abilities and experience will be the perfect fit for our company.
In this role, you will be required to take full ownership over the product life cycle, understand customer needs through research and market data and own and shape the backlog, roadmap and vision of one cross-functional product team.
The starting annual salary for this position is $75,000 to be paid on a semi-monthly basis by direct deposit starting on August 1st, 2019. This salary also includes stock options.
Your employment with [company name] will be on an at-will basis, which means you and the company are free to terminate the employment relationship at any time for any reason. This letter is not a contract or guarantee of employment for a definite amount of time. (Source: Indeed)
As an employee of [company name], you are also eligible for our benefits program, which includes medical insurance, 401(k), and up to two weeks vacation time. Other benefits will be described in more detail in the orientation package.

By signing and returning this letter you will confirm your acceptance of  the offer. Please respond no later than 
 
  <|DATE|>
'''

name=input("enter your name\n")
date=input("enter Date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)