const {library} = require('./library');
const{assert} = require('chai');


describe('library', function () {
    it('should invalid book name', function () {
        assert.throw(()=>{library.calcPriceOfBook([],1998)},Error,"Invalid input");
    });
    it('should invalid book name2', function () {
        assert.throw(()=>{library.calcPriceOfBook(1,1998)},Error,"Invalid input");
    });

    it('should invalid year', function () {
        assert.throw(()=>{library.calcPriceOfBook('book','1998')},Error,"Invalid input");
    });
    it('should invalid year2', function () {
        assert.throw(()=>{library.calcPriceOfBook('book',[])},Error,"Invalid input");
    });
    it('should invalid parameters', function () {
        assert.throw(()=>{library.calcPriceOfBook(1,'1980')},Error,"Invalid input");
    });
    it('should year ltn 1980', function () {
        assert.equal(library.calcPriceOfBook('book1',1977),`Price of book1 is 10.00`)
    });


    it('should year ltn 1980', function () {
        assert.equal(library.calcPriceOfBook('book1',1980),`Price of book1 is 10.00`)
    });
    it('should year gtn 1980', function () {
        assert.equal(library.calcPriceOfBook('book1',1985),`Price of book1 is 20.00`)
    });
    it('should year  1981', function () {
        assert.equal(library.calcPriceOfBook('book1',1981),`Price of book1 is 20.00`)
    });

    it('should with empty arr', function () {
        assert.throw(()=>{library.findBook([],'book1')},Error,"No books currently available")
    });
    it('should with empty arr', function () {
        assert.throw(()=>{library.findBook([],1)},Error,"No books currently available")
    });
    it('should with empty arr', function () {
        assert.throw(()=>{library.findBook([],[])},Error,"No books currently available")
    });
    it('should with valid arr and exist book', function () {
       assert.equal(library.findBook(['book1','book2','book3'],'book2'),"We found the book you want.")
    });
    it('should with valid arr and exist book', function () {
        assert.equal(library.findBook([1,2,3],3),"We found the book you want.")
    });
    it('should with valid arr and not exist book', function () {
        assert.equal(library.findBook(['book1','book2','book3'],'book5'),"The book you are looking for is not here!")
    });
    it('should with valid arr and not exist book', function () {
        assert.equal(library.findBook([1,2,3],'book5'),"The book you are looking for is not here!")
    });
    it('should with valid arr and not exist book', function () {
        assert.equal(library.findBook([1,2,3],[]),"The book you are looking for is not here!")
    });
    it('should with valid arr and not exist book', function () {
        assert.equal(library.findBook(['book1','book2','book3'],1),"The book you are looking for is not here!")
    });
    it('should arrange books with invalid parameter', function () {
            assert.throw(()=>{library.arrangeTheBooks('1')},Error,"Invalid input");
    });
    it('should arrange books with invalid parameter', function () {
        assert.throw(()=>{library.arrangeTheBooks(-1)},Error,"Invalid input");
    });
    it('should arrange books with valid parameter and available space', function () {
        assert.equal(library.arrangeTheBooks(5),"Great job, the books are arranged.");
    });
    it('should arrange books with valid parameter and unavailable space', function () {
        assert.equal(library.arrangeTheBooks(41),"Insufficient space, more shelves need to be purchased.");
    });
    it('should arrange books with valid parameter and unavailable space', function () {
        assert.equal(library.arrangeTheBooks(40),"Great job, the books are arranged.");
    });
});