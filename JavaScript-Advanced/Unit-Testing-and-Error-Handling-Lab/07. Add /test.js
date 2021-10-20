const {createCalculator} = require('./07. Add-Subtract');
const {expect} = require('chai');

describe('createCalculator', function () {
    let instance = {};
    beforeEach(()=>{
        instance = createCalculator();
    })
    it('return add,substract,get', function () {
        expect(instance).to.hasOwnProperty('add')
        expect(instance).to.hasOwnProperty('subtract')
        expect(instance).to.hasOwnProperty('get')
    });
    it('keep sum', function () {
        expect(instance.get()).to.equal(0);
    });
    it('add', function () {
        instance.add(2)
        expect(instance.get()).to.equal(2);
    });
    it('subtract', function () {
        instance.subtract(2)
        expect(instance.get()).to.equal(-2);
    });
    it('add and subtract', function () {
        instance.add(2)
        instance.subtract(3)
        expect(instance.get()).to.equal(-1);
    });
    it('add-string', function () {
        instance.add('2')
        expect(instance.get()).to.equal(2);
    });
    it('subtract-string', function () {
        instance.subtract('2')
        expect(instance.get()).to.equal(-2);
    });
});