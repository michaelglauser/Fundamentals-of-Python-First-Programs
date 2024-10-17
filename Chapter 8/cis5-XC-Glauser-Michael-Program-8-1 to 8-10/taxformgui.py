#Python Programs Chapter 8 Project 1
#Write a GUI-based program that implements the tax calculator program shown in figure 8-2.

from breezypythongui import EasyFrame

STANDARD_DEDUCTION = 10000.0
DEPENDENT_DEDUCTION = 3000.0
TAX_RATE = 0.20

class tax_calculator_gui(EasyFrame):
 

    def __init__(self):
 
        EasyFrame.__init__(self, title="Tax Calculator")

  
        self.addLabel(text="Income", row=0, column=0)
        self.incomeField = self.addFloatField(value="", row=0, column=1)

  
        self.addLabel(text="Dependents", row=1, column=0)
        self.depField = self.addIntegerField(value="", row=1, column=1)

  
        self.addButton(text="Compute", row=2, column=1, command=self.computeTax)

  
        self.addLabel(text="Total tax", row=3, column=0)
        self.taxField = self.addFloatField(value="", row=3, column=1)

    def computeTax(self):
        grossIncome = self.incomeField.getNumber()
        numDependents = self.depField.getNumber()

        taxableIncome = (
            grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
        )

        incomeTax = taxableIncome * TAX_RATE

        self.taxField.setNumber(incomeTax)

def main():
    tax_calculator_gui().mainloop()

if __name__ == "__main__":
    main()
