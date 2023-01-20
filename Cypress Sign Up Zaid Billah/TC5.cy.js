describe('template spec', () => {
    it('Add New User TC 5 Positive', () => {
      cy.visit('https://itera-qa.azurewebsites.net/UserRegister/NewUser')
      cy.wait(3)
      cy.get('#FirstName').type('Tang03')
      cy.wait(3)
      cy.get('#Surname').type('Tang04')
      cy.get('#Username').type('Tang05')
      cy.get('#Password').type('12345')
      cy.get('#ConfirmPassword').type('12345')
      cy.wait(3)
      cy.get('#submit').click()
    })
  })