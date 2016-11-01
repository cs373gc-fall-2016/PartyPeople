import { EventEmitter, SimpleChange, OnChanges, DoCheck } from "@angular/core";
export interface SortEvent {
    sortBy: string | string[];
    sortOrder: string;
}
export interface PageEvent {
    activePage: number;
    rowsOnPage: number;
    dataLength: number;
}
export interface DataEvent {
    length: number;
}
export declare class DataTable implements OnChanges, DoCheck {
    inputData: any[];
    private sortBy;
    private sortOrder;
    rowsOnPage: number;
    activePage: number;
    private mustRecalculateData;
    data: any[];
    onDataChange: EventEmitter<DataEvent>;
    onSortChange: EventEmitter<SortEvent>;
    onPageChange: EventEmitter<PageEvent>;
    getSort(): SortEvent;
    setSort(sortBy: string | string[], sortOrder: string): void;
    getPage(): PageEvent;
    setPage(activePage: number, rowsOnPage: number): void;
    private calculateNewActivePage(previousRowsOnPage, currentRowsOnPage);
    private recalculatePage();
    ngOnChanges(changes: {
        [key: string]: SimpleChange;
    }): any;
    ngDoCheck(): any;
    private fillData();
    private caseInsensitiveIteratee(sortBy);
}
