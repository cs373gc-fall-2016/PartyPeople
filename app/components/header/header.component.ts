import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';


@Component({
	selector: 'pp-header',
	templateUrl: 'app/components/header/header.html',
	styleUrls: ['app/components/header/header.css']
})

export class HeaderComponent {

    private router: Router;

    constructor(private router2: Router, private route: ActivatedRoute){
        this.router = router2;
    }

    searchSubmit(event: Event){
        event.preventDefault();
        var searchText = (<HTMLInputElement>document.getElementById("headerSearchBox")).value;
        let navigationExtras={
            queryParams: {'term': searchText}
        };

        this.router.navigate(['search'],navigationExtras);

        console.log("SEARCH: " + searchText);
        location.reload();
    }
}
