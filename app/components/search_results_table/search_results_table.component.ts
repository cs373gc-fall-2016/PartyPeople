import { Component, OnInit } from '@angular/core';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'candidates-table',
    templateUrl: 'app/components/candidates_table/candidates_table.html',
    providers: [
    	AllServicesService
    ]
})
export class CandidatesTableComponent implements OnInit {
	errorMessage: string;
	title = "Candidates";
	data: any[];

	constructor(private allServicesService: AllServicesService) {}

	ngOnInit() {
		this.getAllCandidates();
	}

	getAllCandidates() {
		this.allServicesService.getAllCandidates().subscribe(
			allCandidates => this.data = allCandidates,
			error => this.errorMessage = <any>error);
		console.log("Getting all candidates.");
	}


}
