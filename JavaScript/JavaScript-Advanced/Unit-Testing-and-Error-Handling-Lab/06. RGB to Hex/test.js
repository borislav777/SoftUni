const {rgbToHexColor} = require('./06. RGB to Hex');
const{expect} = require('chai');
const {describe} = require("mocha");

describe('rgbToHexColor', function () {
    it('Take three integer numbers, representing the red, green, and blue values of RGB color, each within the range [0…255]', function () {

        expect(rgbToHexColor(0,0,'0')).to.equal(undefined);
        expect(rgbToHexColor(0,'1',0)).to.equal(undefined);
        expect(rgbToHexColor('1',0,0)).to.equal(undefined);

    });
    it('missing parameters', function () {
        expect(rgbToHexColor(0)).to.equal(undefined);
    });
    it('take three not valid parameters', function () {
        expect(rgbToHexColor('1','hkhkj','k')).to.equal(undefined);
    });
    it('values out of range', function () {
        expect(rgbToHexColor(-1,0,0)).to.equal(undefined);
        expect(rgbToHexColor(0,-1,0)).to.equal(undefined);
        expect(rgbToHexColor(0,0,-1)).to.equal(undefined);
        expect(rgbToHexColor(-1,-1,-1)).to.equal(undefined);

    });
    it('black', function () {
        expect(rgbToHexColor(0,0,0)).to.equal('#000000');
    });
    it('white', function () {
        expect(rgbToHexColor(255,255,255)).to.equal('#FFFFFF');
    });
    it('larger number', function () {
        expect(rgbToHexColor(256,255,255)).to.equal(undefined);
        expect(rgbToHexColor(255,255,256)).to.equal(undefined);
        expect(rgbToHexColor(256,255,255)).to.equal(undefined);
        expect(rgbToHexColor(256,256,256)).to.equal(undefined);
    });
    it('random color', function () {
        expect(rgbToHexColor(192,192,192)).to.equal('#C0C0C0');
    });
});