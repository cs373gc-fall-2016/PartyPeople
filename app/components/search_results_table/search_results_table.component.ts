import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AllServicesService } from '../../services/allServices.service';
import { Observable } from 'rxjs/Observable';

@Component({
    selector: 'search-results-table',
    templateUrl: 'app/components/search_results_table/search_results_table.html',
    providers: [
    	AllServicesService
    ],
    styles: [
        'app/components/search_results_table/search_results_table.css'
    ]
})

export class SearchResultsTableComponent implements OnInit {
	errorMessage: string;
	title = "Search Results";
	data: any[];
    private searchTerm : string;
    private andSelected = true;

    constructor(private route: ActivatedRoute, private allServicesService: AllServicesService, private router: Router) {}

    ngOnInit() {
        this.route.queryParams.map(params => params['term'] ).subscribe(value => this.searchTerm = value);
        (this.andSelected) ? this.andClicked() : this.orClicked();
    }


	getAllSearchResults(searchType: string) { 
        this.data = [];
		this.allServicesService.getAllSearchResults(this.searchTerm, searchType).subscribe(
			allSearchResults => this.data = allSearchResults,
			error => this.errorMessage = <any>error);
	}

    andClicked() {
        this.andSelected = true;
        (<HTMLButtonElement>document.getElementById("andButton")).style.background = "#E0162B";
        (<HTMLButtonElement>document.getElementById("orButton")).style.background = "#0052A5";
        this.getAllSearchResults("AND");
    }

     orClicked() {
        this.andSelected = false;
        (<HTMLButtonElement>document.getElementById("andButton")).style.background = "#0052A5";
        (<HTMLButtonElement>document.getElementById("orButton")).style.background = "#E0162B";
        this.getAllSearchResults("OR");
    }
}
