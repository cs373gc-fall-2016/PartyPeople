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
	data: any[];

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
