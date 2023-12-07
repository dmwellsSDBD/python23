"""
File: tidbitwithgui.py
Project 8.7

GUI for tidbit program.

Inputs: purchase price and annual interest rate.
"""

from breezypythongui import EasyFrame

class TidbitGUI(EasyFrame):

    def __init__(self):
        """Set up the window and widgets."""
        EasyFrame.__init__(self, title = "Tidbit Loan Scheduler")
        # Input fields
        self.addLabel(text = "Purchase Price", row = 0, column = 0)
        self.priceField = self.addFloatField(value = 0.0, row = 0, column = 1)
        self.addLabel(text = "Annual Interest Rate", row = 1, column = 0)
        self.rateField = self.addFloatField(value = 0.0, row = 1, column = 1)
        # Command button
        self.button = self.addButton(text = "Compute", row = 2, column = 0,
                                     columnspan = 2,
                                     command = self.computeSchedule)
        # Output text box
        self.outputArea = self.addTextArea(text = "", row = 3, column = 0,
                                           columnspan = 2, width = 85,
                                           height = 20)

    def computeSchedule(self):
        """Event handler for the Compute button."""
        purchasePrice = self.priceField.getNumber()
        monthlyPayment = .05 * purchasePrice
        annualRate = self.rateField.getNumber()
        monthlyRate = annualRate / 12
        month = 1
        balance = purchasePrice
        schedule = "Month  Starting Balance  Interest to Pay  Principal to Pay  Payment  Ending Balance\n"
        while balance > 0:
            if monthlyPayment > balance:
                monthlyPayment = balance
                interest = 0
            else:
                interest = balance * monthlyRate
            principal = monthlyPayment - interest
            remaining = balance - monthlyPayment
            schedule += "%2d%15.2f%15.2f%17.2f%17.2f%17.2f\n" % \
                  (month, balance, interest, principal, monthlyPayment, remaining)
            balance = remaining
            month += 1
        self.outputArea.setText(schedule)

def main():
    """Instantiate and pop up the window."""
    TidbitGUI().mainloop()

if __name__ == "__main__":
    main()
