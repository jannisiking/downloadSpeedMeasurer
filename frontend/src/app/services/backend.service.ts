import { Injectable } from '@angular/core';
import {environment} from "../../environments/environment";
import {Measurement} from "../model/measurement";
import {Observable, of} from "rxjs";
import {HttpClient} from "@angular/common/http";

@Injectable({
  providedIn: 'root'
})
export class BackendService {

  baseUrl = `${window.location.protocol}//${window.location.hostname}${window.location.port ? ':' + window.location.port : ''}`;

  constructor(
    private http: HttpClient
  ) { }

  getMeasurements(
    fromTimestamp: Date | null,
    toTimestamp: Date | null
  ): Observable<Measurement[]>{

    let url = `${this.baseUrl}/data`;
    if(fromTimestamp && toTimestamp) url += `?from_timestamp=${fromTimestamp}&to_timestamp=${toTimestamp}`
    if(fromTimestamp && !toTimestamp) url +=  `?from_timestamp=${fromTimestamp}`
    if(!fromTimestamp && toTimestamp) url +=  `?to_timestamp=${toTimestamp}`

    return this.http.get<Measurement[]>(url);
  }
}
