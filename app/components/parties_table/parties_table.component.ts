import { Component, OnInit } from '@angular/core';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'parties-table',
    templateUrl: 'app/components/parties_table/parties_table.html',
    providers: [
    	AllServicesService
    ]
})
export class PartiesTableComponent implements OnInit {
	errorMessage: string;
	title = "Parties";
	data: any[];
	loading = true;

	constructor(private allServicesService: AllServicesService) {}

	ngOnInit() {
		this.getAllParties();
	}

	getAllParties() {
		this.allServicesService.getAllParties().subscribe(
			allParties => {
				this.data = allParties;
				this.loading = false;
			},
			error => this.errorMessage = <any>error)
	}

}
