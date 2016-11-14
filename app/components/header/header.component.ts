import { Component } from '@angular/core';

@Component({
	selector: 'pp-header',
	templateUrl: 'app/components/header/header.html',
	styleUrls: ['app/components/header/header.css']
})
export class HeaderComponent {
    searchSubmit(){
        var searchText = (<HTMLInputElement>document.getElementById("headerSearchBox")).value;
        console.log(searchText);
    }

    updateSearchHref(){
        var searchText = (<HTMLInputElement>document.getElementById("headerSearchBox")).value;
        console.log("Search Text: " + searchText);
        var button = <HTMLAnchorElement>document.getElementById("buttonHref");
        button.href = '/search/' + searchText;
        console.log("button.href: " + button.href);
    }
}
