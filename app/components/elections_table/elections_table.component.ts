import { Component, OnInit } from '@angular/core';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'elections-table',
    templateUrl: 'app/components/elections_table/elections_table.html',
    providers: [
    	AllServicesService
    ]
})
export class ElectionsTableComponent implements OnInit {
	errorMessage: string;
	title = "Elections";
	columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
	data = [
		{"STATE NAME": "Texas", "CAPITAL": "Austin", "POPULATION": "123123123", "GOVERNOR": "asdf", "PARTY IN CONTROL": "reps"},
		{"STATE NAME": "Colorado", "CAPITAL": "Denver", "POPULATION": "987654", "GOVERNOR": "asdfeqwrasdf", "PARTY IN CONTROL": "dems"},
		{"STATE NAME": "Arizona", "CAPITAL": "Phoenix", "POPULATION": "325478951", "GOVERNOR": "someone", "PARTY IN CONTROL": "who knows"}
	];

	constructor(private allServicesService: AllServicesService) {}

	ngOnInit() {
		this.getAllElections();
	}

	getAllElections() {
		this.allServicesService.getAllElections().subscribe(
			allElections => this.data = allElections,
			error => this.errorMessage = <any>error)
	}

}
