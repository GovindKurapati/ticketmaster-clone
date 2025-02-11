import React, { useEffect, useState } from "react";
import {
  Box,
  Flex,
  Spacer,
  Link,
  Button,
  Icon,
  HStack,
  Heading,
  Text,
} from "@chakra-ui/react";
import { FaUser } from "react-icons/fa";
import { EventCard } from "../../components/eventCard";
import useEventStore from "../../store/eventStore";

const Home = () => {
  const { fetchAllEvents, events, loading, error } = useEventStore();

  // Fetch all events when the component mounts
  useEffect(() => {
    fetchAllEvents();
  }, [fetchAllEvents]);

  return (
    <Flex w="100%" flexDirection={"column"}>
      <Flex
        bgRepeat="no-repeat"
        bgSize="cover"
        bgPosition={"50% 0px"}
        bgImage={`url(${events?.length > 0 ? events[0]?.ImageUrl : ""})`}
        textAlign="center"
        py={16}
        px={8}
        w="100%"
        flexDirection={"column"}
        color={"brand.secondary"}
        minHeight={"50vh"}
        justifyContent={"flex-end"}
        overflow="hidden" // Ensure no overflow if content exceeds bounds
        position="relative"
        _before={{
          content: '""',
          position: "absolute",
          top: 0,
          left: 0,
          width: "100%",
          height: "100%",
          bgGradient: "linear(to-r, rgba(0, 0, 0, 0.8), rgba(0, 0, 0, 0) 100%)",
          zIndex: 1, // Overlay above the background image but below content
        }}
      >
        <Flex flexDirection={"column"} maxWidth={"400px"} zIndex={"100"}>
          {/* Disney Logo and Title */}
          <Heading as="h1" fontSize="4xl" mb={4}>
            {events?.length > 0 ? events[0]?.Name : ""}
          </Heading>

          {/* Subtitle */}
          <Text fontSize="xl" mb={6}>
            {events?.length > 0 ? events[0]?.Description : ""}
          </Text>

          {/* Find Tickets Button */}
          <Link href={events?.length > 0 ? `events/${events[0]?.EventID}` : ""}>
            <Button
              size="lg"
              colorScheme="brand.primary"
              bg="brand.primary"
              _hover={{ bg: "brand.primary.900" }}
              px={8}
              py={6}
            >
              Find Tickets
            </Button>
          </Link>
        </Flex>
      </Flex>

      {/* Events Section */}
      <Flex
        w={"100%"}
        flexWrap={"wrap"}
        p="4"
        gap={"4"}
        justifyContent={"space-around"}
      >
        {loading && <Text>Loading...</Text>}
        {error && <Text>Error loading events</Text>}

        {!loading && !error && events?.length > 0 ? (
          events.map((event) => (
            <EventCard
              key={event.EventID}
              title={event.Name}
              description={event.Description}
              date={event.Date}
              eventID={event.EventID}
              image={event.ImageUrl}
            />
          ))
        ) : (
          <Text>No events available</Text>
        )}
      </Flex>
    </Flex>
  );
};

export default Home;
