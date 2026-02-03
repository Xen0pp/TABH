import React from 'react';
import AdminProfileCard from './AdminProfileCard';

const leadership = [
  {
    name: 'Lt. Gen. P.S. Jaggi',
    designation: 'General Officer Commanding (GOC)',
    description: 'Overseeing all strategic and operational aspects of the hostel, ensuring the highest standards of discipline and welfare for all residents.',
    imageUrl: '/placeholder.svg',
    rank: 'goc',
  },
  {
    name: 'Col. Sameer Sharma',
    designation: 'Officer-in-Command (OIC)',
    description: 'Responsible for the day-to-day management and administration of the hostel, reporting directly to the GOC.',
    imageUrl: '/placeholder.svg',
    rank: 'oic',
  },
  {
    name: 'Maj. R.K. Singh',
    designation: '2nd Officer-in-Command (2-OIC)',
    description: 'Assisting the OIC in all administrative duties and overseeing the welfare of the hostelers.',
    imageUrl: '/placeholder.svg',
    rank: '2-oic',
  },
  {
    name: 'Mr. Alok Kumar',
    designation: 'Warden',
    description: 'The primary point of contact for all hostel residents, managing discipline, room allocation, and daily routines.',
    imageUrl: '/placeholder.svg',
    rank: 'warden',
  },
];

const officeStaff = [
  { name: 'Mr. Ramesh Gupta', designation: 'Head Clerk', imageUrl: '/placeholder.svg' },
  { name: 'Mr. Suresh Kumar', designation: 'Accountant', imageUrl: '/placeholder.svg' },
  { name: 'Mrs. Sunita Sharma', designation: 'Administrative Assistant', imageUrl: '/placeholder.svg' },
];

const guards = [
  { name: 'Mr. Ram Singh', designation: 'Head Guard', imageUrl: '/placeholder.svg' },
  { name: 'Mr. Shyam Lal', designation: 'Guard (Gate 1)', imageUrl: '/placeholder.svg' },
  { name: 'Mr. Mohan Kumar', designation: 'Guard (Gate 2)', imageUrl: '/placeholder.svg' },
];

const AdministrationContainer = () => {
  return (
    <div className="bg-gray-50 min-h-screen p-4 sm:p-6 md:p-8 font-serif">
      <div className="max-w-7xl mx-auto">
        <div className="text-center mb-16">
          <h1 className="text-4xl md:text-5xl font-bold text-gray-900 font-merriweather">TABH Administration</h1>
          <p className="text-lg text-gray-600 mt-2">Administrative Leadership & Hostel Governance</p>
        </div>

        <div className="relative max-w-3xl mx-auto">
          <div className="absolute left-1/2 -ml-px w-0.5 h-full bg-gray-300" aria-hidden="true"></div>
          <div className="space-y-12">
            {leadership.map((person) => (
              <div key={person.name} className="relative">
                <AdminProfileCard {...person} />
              </div>
            ))}
          </div>
        </div>

        <div className="mt-20">
          <h2 className="text-3xl font-bold text-center text-gray-900 font-merriweather mb-10">Supporting Administration</h2>
          <h3 className="text-2xl font-semibold text-center text-gray-800 mb-8">Office Staff</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
            {officeStaff.map((person) => (
              <AdminProfileCard key={person.name} {...person} />
            ))}
          </div>

          <h3 className="text-2xl font-semibold text-center text-gray-800 mt-16 mb-8">Guards</h3>
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8 max-w-5xl mx-auto">
            {guards.map((person) => (
              <AdminProfileCard key={person.name} {...person} />
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AdministrationContainer;
