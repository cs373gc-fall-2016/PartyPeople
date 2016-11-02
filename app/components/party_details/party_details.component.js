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
var PartyDetailsComponent = (function () {
    function PartyDetailsComponent(route) {
        this.route = route;
        this.stateName = "Party Name";
        this.columns = ["STATE NAME", "CAPITAL", "POPULATION", "GOVERNOR", "PARTY IN CONTROL"];
        this.data = { "STATE NAME": "Texas", "CAPITAL": "Austin", "POPULATION": "123123123", "GOVERNOR": "asdf", "PARTY IN CONTROL": "reps" };
    }
    PartyDetailsComponent.prototype.ngOnInit = function () {
        var _this = this;
        this.sub = this.route.params.subscribe(function (params) {
            _this.id = +params['id'];
            // In a real app: dispatch action to load the details here.
        });
    };
    PartyDetailsComponent.prototype.ngOnDestroy = function () {
        this.sub.unsubscribe();
    };
    PartyDetailsComponent = __decorate([
        core_1.Component({
            selector: 'party-details',
            templateUrl: 'app/components/party_details/party_details.html',
        }), 
        __metadata('design:paramtypes', [router_1.ActivatedRoute])
    ], PartyDetailsComponent);
    return PartyDetailsComponent;
}());
exports.PartyDetailsComponent = PartyDetailsComponent;
//# sourceMappingURL=party_details.component.js.map