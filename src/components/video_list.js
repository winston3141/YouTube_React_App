import React from 'react';
import NavBarItem from './nav-bar-item';

const VideoList = (props) => {
	const navBarItems = props.videos.map ((video) => {
		return (
			<NavBarItem
			  onVideoSelect={props.onVideoSelect}
			  key={video.etag}
			  video={video} />
		);
	});

	return (
		<ul className="col-md-4 list-group">
			{navBarItems}
		</ul>
	);
};

export default VideoList;