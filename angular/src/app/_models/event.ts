import { User } from './index'
export class Event {
    storage: number;
    name: string;
    start_time: string;
    end_time: string;
    location_lat:number;
    location_lon:number;
}

export class Storage{
    name: string;
    location_lon: number;
    location_lat: number;
}

export class Message{
    id:number;
    message_from: User;
    message_to: User;

    message_body: string;
    is_read: number;
}