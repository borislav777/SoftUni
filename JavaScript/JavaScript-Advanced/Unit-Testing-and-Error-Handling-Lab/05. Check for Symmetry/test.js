const {isSymmetric} = require('./05. Check for Symmetry');
const {expect} = require('chai');

describe('isSymetric', () => {
    it('Take an array as an argument', function () {
        expect(isSymmetric([1,2,2,1])).to.be.true;
    });
    it('Return false for any input that isn’t of the correct type',  () => {

        expect(isSymmetric('abba')).to.be.false;




    });
    it('Return false for number input',()=>{
        expect(isSymmetric(1)).to.be.false;
    })
    it('arrays are non-symmetric', function () {
        expect(isSymmetric([1,2,3,5])).to.be.false;
    });
    it('Take an array-strings', function () {
        expect(isSymmetric(['a','b','b','a'])).to.be.true;
    });
    it('Take an array with different types', function () {
        expect(isSymmetric([1,2,2,'1'])).to.be.false;
    });

});