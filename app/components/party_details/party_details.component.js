"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var router_1 = require('@angular/router');
var allServices_service_1 = require('../../services/allServices.service');
var PartyDetailsComponent = (function () {
    function PartyDetailsComponent(route, allServicesService) {
        this.route = route;
        this.allServicesService = allServicesService;
        this.data = {};
        this.image = {};
    }
    PartyDetailsComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.sub = this.route.params.subscribe(function (params) {
            _this.id = +params['id'];
            _this.allServicesService.getPartyDetails(_this.id).subscribe(function (partyInfo) {
                _this.data = partyInfo,
                    _this.allServicesService.getImageData(partyInfo.name).subscribe(function (imageData) { return _this.image = imageData; }, function (error) { return _this.errorMessage = error; });
            });
        }, function (error) { return _this.errorMessage = error; });
    };
    PartyDetailsComponent.prototype.ngOnDestroy = function () {
        this.sub.unsubscribe();
    };
    PartyDetailsComponent = __decorate([
        core_1.Component({
            selector: 'party-details',
            templateUrl: 'app/components/party_details/party_details.html',
            providers: [
                allServices_service_1.AllServicesService
            ]
        }), 
        __metadata('design:paramtypes', [router_1.ActivatedRoute, allServices_service_1.AllServicesService])
    ], PartyDetailsComponent);
    return PartyDetailsComponent;
}());
exports.PartyDetailsComponent = PartyDetailsComponent;
//# sourceMappingURL=party_details.component.js.map