import { Component, OnInit } from '@angular/core';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'states-table',
    templateUrl: 'app/components/states_table/states_table.html',
    providers: [
    	AllServicesService
    ]
})
export class StatesTableComponent implements OnInit {
	errorMessage: string;
	title = "States";
	data: any[];

	constructor(private allServicesService: AllServicesService) {}

	ngOnInit() {
		this.getAllStates();
	}

	getAllStates() {
		this.allServicesService.getAllStates().subscribe(
			allStates => this.data = allStates,
			error => this.errorMessage = <any>error)
	}

}
