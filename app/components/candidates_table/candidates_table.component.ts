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
	title = "Candidate";
	columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
	data = [
		{
 "contact": "candidate1@us.gov", 
 "dob": null, 
 "election_id": null, 
 "elections": null, 
 "id": 1, 
 "job": "politician", 
 "name": "Candidate_1", 
 "party": null, 
 "party_id": null, 
 "poll": 50.0, 
 "state_id": null, 
 "states": null
},
{
 "contact": "candidate2@us.gov", 
 "dob": null, 
 "election_id": null, 
 "elections": null, 
 "id": 1, 
 "job": "politician", 
 "name": "Candidate_1", 
 "party": null, 
 "party_id": null, 
 "poll": 50.0, 
 "state_id": null, 
 "states": null
}
	];

	constructor(private allServicesService: AllServicesService) {}

	ngOnInit() {
		this.getAllCandidates();
	}

	getAllCandidates() {
		this.allServicesService.getAllCandidates().subscribe(
			allCandidates => this.data = allCandidates,
			error => this.errorMessage = <any>error);
		console.log("Canidates Data: " + this.data);
	}


}
