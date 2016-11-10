import { Component, OnInit, OnDestroy } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { AllServicesService } from '../../services/allServices.service';

@Component({
    selector: 'party-details',
    templateUrl: 'app/components/party_details/party_details.html',
    providers: [
    	AllServicesService
    ]
})
export class PartyDetailsComponent implements OnInit, OnDestroy {
	errorMessage: string;
	id: number;
	private sub: any;

	data = {};

	constructor(private route: ActivatedRoute, private allServicesService: AllServicesService) {}

	ngOnInit() {
	    this.sub = this.route.params.subscribe(params => {
	       this.id = +params['id'];

	       this.allServicesService.getPartyDetails(this.id).subscribe(
			partyInfo => this.data = partyInfo,
			error => this.errorMessage = <any>error)
	    });
	  }

	ngOnDestroy() {
    	this.sub.unsubscribe();
  	}

}