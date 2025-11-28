import {useEffect, useState} from "react";

interface JobListing {
    id:number;
    title:string;
    description:string;
    created_at:string;
}
export default function JobsList() { 
    const [jobs, setJobs] = useState<JobListing[]>([]);
    const [loading, setLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        fetch ('http://localhost:8000/api/job-listings/')
        .then((response) => response.json())
        .then((data) => {
            setJobs(data);
            setLoading(false);
        })
        .catch((error) =>  console.error("Error:", error));
           
        }, []);
        if (loading) {
            return <div>loading...</div>;
        }
        if (error) {
        return <div>Error: {error}</div>;
    }
    return (
        <div>
            <h1>Jobs Listing</h1>
            {jobs.length === 0 ? (
                <p>No jobs found that matches your requirements.  </p> )
                : (
                    <ul>
                        {jobs.map((job) => (
                            <li key={job.id}>
                                <strong>{job.title} </strong>: {job.description}
                            </li>
                        ))}
                    </ul>
                    )}
        </div>
    );

        
    
}
    