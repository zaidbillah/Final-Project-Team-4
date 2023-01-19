describe('template spec', () => {
    it('Sign In TC 1', () => {
      cy.visit('https://itera-qa.azurewebsites.net/')
      cy.wait(3)
      cy.get('.form-inline > .navbar-nav > :nth-child(1) > .nav-link').click()
      cy.wait(3)
      
    })
  })