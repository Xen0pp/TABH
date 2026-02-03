import React from 'react';
import { Star, Shield, User } from 'lucide-react';

const rankInsignias = {
  goc: <Star className="w-6 h-6 text-yellow-500" />,
  oic: <Shield className="w-6 h-6 text-blue-800" />,
  '2-oic': <Shield className="w-5 h-5 text-blue-600" />,
  warden: <User className="w-5 h-5 text-gray-700" />,
};

const cardConfig = {
  goc: {
    card: 'md:flex-row max-w-3xl mx-auto bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden',
    imageContainer: 'md:w-1/3',
    image: 'h-full w-full object-cover',
    textContainer: 'md:w-2/3 p-8',
    name: 'text-4xl font-bold text-gray-900 font-merriweather',
    designation: 'text-xl font-semibold text-yellow-600 mt-1',
  },
  leadership: {
    card: 'md:flex-row max-w-2xl mx-auto bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden',
    imageContainer: 'md:w-1/3',
    image: 'h-full w-full object-cover',
    textContainer: 'md:w-2/3 p-6',
    name: 'text-3xl font-bold text-gray-800 font-merriweather',
    designation: 'text-lg font-semibold text-blue-800 mt-1',
  },
  staff: {
    card: 'flex-col text-center bg-white rounded-lg shadow-md border border-gray-200 p-6',
    imageContainer: 'w-full',
    image: 'w-28 h-28 rounded-full mx-auto border-4 border-gray-300',
    textContainer: 'mt-4',
    name: 'text-xl font-bold text-gray-800',
    designation: 'text-md font-semibold text-gray-600',
  },
};

const AdminProfileCard = ({ name, designation, description, imageUrl, rank = 'staff' }) => {
  const isLeadership = ['goc', 'oic', '2-oic', 'warden'].includes(rank);
  const config = rank === 'goc' ? cardConfig.goc : isLeadership ? cardConfig.leadership : cardConfig.staff;

  return (
    <div className={`flex ${config.card}`}>
      <div className={config.imageContainer}>
        <img src={imageUrl} alt={`Formal portrait of ${name}`} className={config.image} />
      </div>
      <div className={config.textContainer}>
        <div className="flex items-center gap-3">
          {isLeadership && rankInsignias[rank]}
          <h3 className={config.name}>{name}</h3>
        </div>
        <p className={config.designation}>{designation}</p>
        {description && <p className="text-gray-600 mt-4 text-base leading-relaxed">{description}</p>}
      </div>
    </div>
  );
};

export default AdminProfileCard;
