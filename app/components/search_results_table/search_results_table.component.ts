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

    constructor(private route: ActivatedRoute, private allServicesService: AllServicesService, private router : Router) { }

    ngOnInit() {
        this.route.queryParams.map(params => params['term'] ).subscribe(value => this.searchTerm = value);

        this.getAllSearchResults();
      }


	getAllSearchResults() { 
        // TODO: Add switch and toggle between AND and OR results
		this.allServicesService.getAllSearchResults(this.searchTerm,"AND").subscribe(
			allSearchResults => this.data = allSearchResults,
			error => this.errorMessage = <any>error);
	}


}
