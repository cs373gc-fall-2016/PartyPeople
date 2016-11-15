import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { AllServicesService } from '../../services/allServices.service';
import { Observable } from 'rxjs/Observable';

@Component({
    selector: 'search-results-table',
    templateUrl: 'app/components/search_results_table/search_results_table.html',
    providers: [
    	AllServicesService
    ]
})

export class SearchResultsTableComponent implements OnInit, OnDestroy {
	errorMessage: string;
	title = "Search Results";
	data: any[];

    term: Observable<string>;
    private sub: any;
    private router : Router;
    private searchTerm : string;

    constructor(private route: ActivatedRoute, private allServicesService: AllServicesService, private router2 : Router) {
        this.router = router2;
    }

    ngOnInit() {
        this.route.queryParams.map(params => params['term'] ).subscribe(value => this.searchTerm = value);

        this.getAllSearchResults();
      }

    ngOnDestroy() {
        this.sub.unsubscribe();
    }

	getAllSearchResults() { 
    //get search terms from search box
    //what about all other special characters
		this.allServicesService.getAllSearchResults("Texas","AND").subscribe(
			allSearchResults => this.data = allSearchResults,
			error => this.errorMessage = <any>error);
	}


}
