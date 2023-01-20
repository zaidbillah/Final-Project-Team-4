describe('template spec', () => {
    it('Add New User TC 2 Positive', () => {
      cy.visit('https://itera-qa.azurewebsites.net/UserRegister/NewUser')
      cy.wait(3)
      cy.get('#FirstName').type('Zaid')
      cy.wait(3)
      cy.get('#Surname').type('Billah')
      cy.get('#E_post').type('zaidbillah@gmail.com')
      cy.get('#Mobile').type('1234456')
      cy.get('#Username').type('Tang02')
      cy.get('#Password').type('Gajahduduk2023!')
      cy.get('#ConfirmPassword').type('Gajahduduk2023!')
      cy.wait(3)
      cy.get('#submit').click()
    })
  })