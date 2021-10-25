const {cinema} = require('./cinema');
const {assert,expect} = require('chai');

describe('Cinema', function () {
    it('should empty arr', function () {
        assert.equal(cinema.showMovies([]),'There are currently no movies to show.')
    });
    it('should empty arr', function () {
        assert.equal(cinema.showMovies(''),'There are currently no movies to show.')
    });

    it('should valid arr', function () {
        assert.equal(cinema.showMovies(['KIng','KOng','Sample']),'KIng, KOng, Sample')
    });
    it('should invalid arr', function () {
        assert.equal(cinema.showMovies([1,2,3,4,5]),'1, 2, 3, 4, 5')
    });
    it('should valid arr', function () {
        assert.equal(cinema.showMovies([{},{}]),'[object Object], [object Object]')
    });
    it('should with valid projection', function () {
        assert.equal(cinema.ticketPrice('Premiere'),12.00)
    });
    it('should with valid projection2', function () {
        assert.equal(cinema.ticketPrice('Normal'),7.50)
    });
    it('should with valid projection3', function () {
        assert.equal(cinema.ticketPrice('Discount'),5.50)
    });
    it('should with invalid projection', function () {
        assert.throw(()=>{cinema.ticketPrice('Student')},Error,'Invalid projection type.')
    });
    it('should with invalid projection', function () {
        assert.throw(()=>{cinema.ticketPrice(1)},Error,'Invalid projection type.')
    });
    it('should with invalid projection', function () {
        assert.throw(()=>{cinema.ticketPrice({})},Error,'Invalid projection type.')
    });
    it('should with invalid projection', function () {
        assert.throw(()=>{cinema.ticketPrice([])},Error,'Invalid projection type.')
    });
    it('should with invalid projection', function () {
        assert.throw(()=>{cinema.ticketPrice(1)},Error,'Invalid projection type.')
    });
    it('should with invalid projection', function () {
        assert.throw(()=>{cinema.ticketPrice([])},Error,'Invalid projection type.')
    });
    it('should swap seats with string parameters', function () {
        assert.equal(cinema.swapSeatsInHall('1',[]),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one string parameters', function () {
        assert.equal(cinema.swapSeatsInHall('1',1),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one string parameters', function () {
        assert.equal(cinema.swapSeatsInHall('a',2),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one string parameters', function () {
        assert.equal(cinema.swapSeatsInHall(5,'b'),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one string parameters', function () {
        assert.equal(cinema.swapSeatsInHall(3,[]),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one string parameters', function () {
        assert.equal(cinema.swapSeatsInHall(3),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one edge parameters', function () {
        assert.equal(cinema.swapSeatsInHall(0,1),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one edge parameters', function () {
        assert.equal(cinema.swapSeatsInHall(1,0),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one edge parameters2', function () {
        assert.equal(cinema.swapSeatsInHall(2,21),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with one edge parameters2', function () {
        assert.equal(cinema.swapSeatsInHall(21,1),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with equals parameters2', function () {
        assert.equal(cinema.swapSeatsInHall(2,2),"Unsuccessful change of seats in the hall.")
    });
    it('should swap seats with valid parameters', function () {
        assert.equal(cinema.swapSeatsInHall(1,20),"Successful change of seats in the hall.")
    });
    it('should swap seats with valid parameters', function () {
        assert.equal(cinema.swapSeatsInHall(5,10),"Successful change of seats in the hall.")
    });
    it('should swap seats with valid parameters', function () {
        assert.equal(cinema.swapSeatsInHall(-5,10),"Successful change of seats in the hall.")
    });
    it('should swap seats with valid parameters', function () {
        assert.equal(cinema.swapSeatsInHall(5,-10),"Successful change of seats in the hall.")
    });

});