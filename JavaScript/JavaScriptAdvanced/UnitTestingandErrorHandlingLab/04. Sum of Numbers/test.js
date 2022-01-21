let {sum} = require('./04. Sum of Numbers');
const {expect} = require('chai');

describe('Sum of Numbers', () => {
    it('Take an array of numbers as an argument', function () {
        expect(sum([1, 2])).to.equal(3)

    });
});