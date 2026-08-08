"use client";

import {
  createContext,
  useContext,
  useState,
  ReactNode,
} from "react";

interface SessionContextType {
  selectedMeeting: number;
  setSelectedMeeting: React.Dispatch<React.SetStateAction<number>>;

  selectedSession: number;
  setSelectedSession: React.Dispatch<React.SetStateAction<number>>;
}

const SessionContext = createContext<
  SessionContextType | undefined
>(undefined);

export function SessionProvider({
  children,
}: {
  children: ReactNode;
}) {
  const [selectedMeeting, setSelectedMeeting] =
    useState(1229);

  const [selectedSession, setSelectedSession] =
    useState(9472);

  return (
    <SessionContext.Provider
      value={{
        selectedMeeting,
        setSelectedMeeting,
        selectedSession,
        setSelectedSession,
      }}
    >
      {children}
    </SessionContext.Provider>
  );
}

export function useSession() {
  const context = useContext(SessionContext);

  if (!context) {
    throw new Error(
      "useSession must be used inside SessionProvider"
    );
  }

  return context;
}