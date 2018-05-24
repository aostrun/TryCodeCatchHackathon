export class Event {
    storage: number;
    name: string;
    start_time: string;
    end_time: string;
}

export class Storage{
    name: string;
    location_lon: number;
    location_lat: number;
}

export class Message{
    id:number;
    message_from_user: number;
    message_to_user: number;
    message_body: string;
    is_read: number;
}