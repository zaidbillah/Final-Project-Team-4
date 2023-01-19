describe('template spec', () => {
    it('Add New User TC 3 Negative', () => {
      cy.visit('https://itera-qa.azurewebsites.net/UserRegister/NewUser')
      cy.wait(3)
      cy.get('#Username').type('Tang02')
      cy.get('#Password').type('Gajahduduk2023!')
      cy.wait(3)
      cy.get('#submit').click()
    })
  })