import { ElementRef, AfterViewInit, OnDestroy, Renderer } from '@angular/core';
import { DomHandler } from '../dom/domhandler';
import { MenuItem } from '../common/api';
import { Router } from '@angular/router';
export declare class ContextMenuSub {
    domHandler: DomHandler;
    router: Router;
    contextMenu: ContextMenu;
    item: MenuItem;
    root: boolean;
    constructor(domHandler: DomHandler, router: Router, contextMenu: ContextMenu);
    activeItem: any;
    activeLink: any;
    onItemMouseEnter(event: any, item: any, menuitem: any): void;
    onItemMouseLeave(event: any, link: any): void;
    itemClick(event: any, item: MenuItem): void;
    listClick(event: any): void;
    position(sublist: any, item: any): void;
}
export declare class ContextMenu implements AfterViewInit, OnDestroy {
    el: ElementRef;
    domHandler: DomHandler;
    renderer: Renderer;
    model: MenuItem[];
    global: boolean;
    style: any;
    styleClass: string;
    visible: boolean;
    container: any;
    documentClickListener: any;
    documentRightClickListener: any;
    constructor(el: ElementRef, domHandler: DomHandler, renderer: Renderer);
    ngAfterViewInit(): void;
    show(event: MouseEvent): void;
    hide(): void;
    position(event: MouseEvent): void;
    unsubscribe(item: any): void;
    ngOnDestroy(): void;
}
export declare class ContextMenuModule {
}
