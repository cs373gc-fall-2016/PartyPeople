import { Component, OnInit } from '@angular/core';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'search-results-table',
    templateUrl: 'app/components/search_results_table/search_results_table.html',
    providers: [
    	AllServicesService
    ]
})

export class SearchResultsTableComponent implements OnInit {
	errorMessage: string;
	title = "Search Results";
	data: any[];

	constructor(private allServicesService: AllServicesService) {}

	ngOnInit() {
		this.getAllSearchResults();
	}

	getAllSearchResults() { 
    //get search terms from search box
    //what about all other special characters
		this.allServicesService.getAllSearchResults("Texas","AND").subscribe(
			allSearchResults => this.data = allSearchResults,
			error => this.errorMessage = <any>error);
	}


}
